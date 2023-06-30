"""
Config module for get|set|load|export settings
"""

__version__ = '2.0.0'


from copy import deepcopy


class Config:
    """ Class of global config """
    def __init__(self):
        """ Init. Set defaults """
        self.__settings = {}  # settings dict

    def __getattr__(self, attr):
        """ If exist attr, returned attr. Else returned section """
        if attr in self.__dict__:
            return self.__dict__[attr]

        return Section(self.get_section(attr))

    def set(self, section: str, setting: str, value: str):
        """ Create or rewrited section, setting, value """

        # convert to str type
        section, setting, value = str(section), str(setting), str(value)

        # if 'section' not exist, create it
        if section not in self.__settings.keys():
            self.__settings[section] = {}

        self.__settings[section][setting] = value

    def get(self, section: str, setting: str, default: str = None) -> str:
        """ get setting. if setting not found - return '' """

        # convert to str type
        section, setting = str(section), str(setting)

        if section in self.__settings and setting in self.__settings[section]:
            return self.__settings[section][setting]

        if default or default == '':
            return str(default)

        raise KeyError(f'not found "{section}" "{setting}" in settings')

    def get_settings(self) -> dict:
        """ Return deep copy if self.__settings """
        return deepcopy(self.__settings)

    def get_section(self, section) -> dict:
        """ return deep copy dict {setting: value, ...} """
        return deepcopy(self.__settings[section])

    def clear(self):
        """ clear settings """
        self.__settings = {}

    def __str__(self) -> str:
        """ Return str for print """
        out_str = ''
        for section in self.__settings:
            for setting in self.__settings[section]:
                value = self.__settings[section][setting]
                out_str += (f'[{section}] {setting} = {value}\n')
        return out_str

    def load_file(self,
                  config_file: str,
                  comment: str = '#',
                  default_section: str = 'main',
                  except_if_error: bool = False,
                  out=print,
                  ) -> bool:
        ok = True

        try:
            with open(config_file, 'r') as file:
                # считать все строки файла в список
                lines = file.readlines()  # грязный список

                # удаляем переводы строк, табы заменяем пробелами
                for index in range(len(lines)):
                    lines[index] = lines[index].replace('\n', '')
                    lines[index] = lines[index].replace('\t', ' ')

                # удалить комментарии по правую часть строки
                # удалить строки, начинающиеся с комментария
                for index in range(len(lines)):
                    if comment in lines[index]:
                        lines[index] = lines[index].split(comment)[0].strip()

                for index in range(len(lines)):
                    lines[index] = lines[index].strip()

                # удаляем пустые строки из списка
                while "" in lines:
                    lines.remove("")

                # проходим по списку,
                # если встречаем разделитель, делим элемент на 2,
                # и загружаем key:value в словарь
                section = default_section
                for line in lines:
                    if line[0] == '[' and line[-1] == ']':
                        section = line[1:-1].strip()
                    if '=' in line:
                        # разделить с макс. кол-вом делений: 1
                        settings_pair = line.split('=', maxsplit=1)
                        # Удаляем пробелы в начале и конце
                        settings_pair[0] = settings_pair[0].strip()
                        settings_pair[1] = settings_pair[1].strip()

                        self.set(section=default_section,
                                 setting=settings_pair[0],
                                 value=settings_pair[1],
                                 )
        except FileNotFoundError:
            ok = False
            error_msg = f'Файл {config_file} не найден!'

            if except_if_error:
                raise FileNotFoundError(error_msg)
            else:
                out(error_msg)

        except IsADirectoryError:
            ok = False
            error_msg = f'{config_file} - это каталог!'

            if except_if_error:
                raise IsADirectoryError(error_msg)
            else:
                out(error_msg)

        return ok

    def export_file(self,
                    config_file: str,
                    out=print,
                    ) -> bool:
        """ export to file all sections, cettings and values """

        ok = True

        try:
            with open(config_file, 'w') as file:
                for section in self.__settings:
                    file.write(f'[{section}]\n')
                    for setting in self.__settings[section]:
                        if len(self.__settings[section][setting]) > 0:
                            value = self.__settings[section][setting]
                            file.write(f'{setting} = {value}\n')
                    file.write('\n\n')

        except Exception:
            out(f'Ошибка записи в файл {config_file}')
            ok = False

        return ok

    def load_env_vars():
        pass


class Section:
    """
    Section class.
    Init need dict 'section dict' ({key:value, ...}),
    create namespace, available in object.<key>
    object.<key> return str value
    """
    def __init__(self, section: dict):
        for setting in section:
            setattr(self, setting, section[setting])

    def __getattr__(self, attr):
        """
        If exist attr, returned attr.
        Else returned section
        """
        if attr in self.__dict__:
            return self.__dict__[attr]

        raise AttributeError(f'no attr "{attr}"')
