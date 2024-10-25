from typing import Dict

class PeopleRegisterController:
    def register(self, new_person_informations: Dict) -> Dict:
        try:
            self.__validate_fields(new_person_informations)
            self.__create_person_entity_and_store(new_person_informations)
            response = self.__format_response(new_person_informations)
            return {"success": True, "message": response}
        except Exception as exception:
            return {"success": False, "error": str(exception)}

    def __validate_fields(self, new_person_informations: Dict) -> None:
        if not isinstance(new_person_informations.get("name"), str):
            raise Exception('Campo nome incorreto!')
        
        if not isinstance(new_person_informations.get("age"), int):
            raise Exception('Campo Idade Incorreto!')

        if not isinstance(new_person_informations.get("height"), int):
            raise Exception('Campo Altura Incorreto!')

    def __format_response(self, new_person_informations: Dict) -> Dict:
        return {
            "count": 1,
            "type": "Person",
            "attributes": new_person_informations
        }


    
    
