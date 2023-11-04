
class Customer:
    def __init__(self, pin, contract, password, first_name, last_name):
        self.__pin = pin
        self.__contract = contract
        self.__password = password
        self.__first_name = first_name
        self.__last_name = last_name
        self.__short_salutation = ''
        self.__title = ''
        self.__country = ''
        self.__state = ''
        self.__zip = ''
        self.__community = ''
        self.__community_part = ''
        self.__street = ''
        self.__house_number = ''
        self.__email = ''
        self.__phone_number = ''
        self.__send_email = ''
        self.__partner = ''
        self.__qr_link = ''
        self.__counters_list = []

    @property
    def get_counters(self):
        return self.__counters_list

    def add_counter(self, id, number, obis_code, obis_code_short_name, min_value, max_value, last_value):
        counter = Counter(id, number, obis_code, obis_code_short_name, min_value, max_value, last_value)
        self.__counters_list.append(counter)

    def set_communication(self, email, phone_number, send_email):
        self.__email = email
        self.__phone_number = phone_number
        self.__send_email = send_email

    @property
    def get_communication(self):
        return self.__email, self.__phone_number, self.__send_email

    def set_address(self, country, state, zip, community, community_part, street, house_number):
        self.__country = country
        self.__state = state
        self.__zip = zip
        self.__community = community
        self.__community_part = community_part
        self.__street = street
        self.__house_number = house_number

    @property
    def get_address(self):
        return self.__country, self.__state, self.__zip, self.__community, self.__community_part, self.__street, self.__house_number

    @property
    def pin(self):
        return self.__pin

    @pin.setter
    def pin(self, value):
        self.__pin = value

    @property
    def contract(self):
        return self.__contract

    @contract.setter
    def contract(self, value):
        self.__contract = value

    @property
    def password(self):
        return self.__password

    @password.setter
    def password(self, value):
        self.__password = value

    @property
    def first_name(self):
        return self.__first_name

    @first_name.setter
    def first_name(self, value):
        self.__first_name = value

    @property
    def last_name(self):
        return self.__last_name

    @last_name.setter
    def last_name(self, value):
        self.__last_name = value

    @property
    def short_salutation(self):
        return self.__short_salutation

    @short_salutation.setter
    def short_salutation(self, value):
        self.__short_salutation = value

    @property
    def title(self):
        return self.__title

    @title.setter
    def title(self, value):
        self.__title = value

    @property
    def country(self):
        return self.__country

    @country.setter
    def country(self, value):
        self.__country = value

    @property
    def state(self):
        return self.__state

    @state.setter
    def state(self, value):
        self.__state = value

    @property
    def zip(self):
        return self.__zip

    @zip.setter
    def zip(self, value):
        self.__zip = value

    @property
    def community(self):
        return self.__community

    @community.setter
    def community(self, value):
        self.__community = value

    @property
    def community_part(self):
        return self.__community_part

    @community_part.setter
    def community_part(self, value):
        self.__community_part = value

    @property
    def street(self):
        return self.__street

    @street.setter
    def street(self, value):
        self.__street = value

    @property
    def house_number(self):
        return self.__house_number

    @house_number.setter
    def house_number(self, value):
        self.__house_number = value

    @property
    def email(self):
        return self.__email

    @email.setter
    def email(self, value):
        self.__email = value

    @property
    def phone_number(self):
        return self.__phone_number

    @phone_number.setter
    def phone_number(self, value):
        self.__phone_number = value

    @property
    def send_email(self):
        return self.__send_email

    @send_email.setter
    def send_email(self, value):
        self.__send_email = value

    @property
    def partner(self):
        return self.__partner

    @partner.setter
    def partner(self, value):
        self.__partner = value

    @property
    def qr_link(self):
        return self.__qr_link

    @qr_link.setter
    def qr_link(self, value):
        self.__qr_link = value


class Counter:
    def __init__(self, id, number, obis_code, obis_code_short_name, min_value, max_value, last_value):
        self.__id = id
        self.__number = number
        self.__obis_code = obis_code
        self.__obis_code_short_name = obis_code_short_name
        self.__min_value = min_value
        self.__max_value = max_value
        self.__last_value = last_value
        self.__obis_code_full_name = ''

    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, value):
        self.__id = value

    @property
    def number(self):
        return self.__number

    @number.setter
    def number(self, value):
        self.__number = value

    @property
    def obis_code(self):
        return self.__obis_code

    @obis_code.setter
    def obis_code(self, value):
        self.__obis_code = value

    @property
    def obis_code_short_name(self):
        return self.__obis_code_short_name

    @obis_code_short_name.setter
    def obis_code_short_name(self, value):
        self.__obis_code_short_name = value

    @property
    def obis_code_full_name(self):
        return self.__obis_code_full_name

    @obis_code_full_name.setter
    def obis_code_full_name(self, value):
        self.__obis_code_full_name = value

    @property
    def min_value(self):
        return self.__min_value

    @min_value.setter
    def min_value(self, value):
        self.__min_value = value

    @property
    def max_value(self):
        return self.__max_value

    @max_value.setter
    def max_value(self, value):
        self.__max_value = value

    @property
    def last_value(self):
        return self.__last_value

    @last_value.setter
    def last_value(self, value):
        self.__last_value = value
