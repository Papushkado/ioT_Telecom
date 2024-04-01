from pydantic import BaseModel

class Client(BaseModel):
    name: str
    firstname : str
    age : int
    mail_adress : str

    contact_name : str
    contact_phone_number : int

    alcohol_threshold : int

