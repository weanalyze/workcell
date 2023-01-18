from pydantic import BaseModel
from fastapi.encoders import jsonable_encoder
from workcell.core import get_spec



def spec(self) -> str:
    print('1. __dict__')
    print(self._output_type.__dict__)
    print('2. __fields__')
    print(self._output_type.__fields__)
    print('3. __fields__ json')
    print(jsonable_encoder(self._output_type))
    print('4. __fields__ json dir')
    print(jsonable_encoder(self._output_type.__fields__['short_text'].dict()))        
    spec = {
        "name": self._name,
        "version": self._version,
        "description": self._description,
        "spec": {
            "input": self._input_type.__fields__,
            "output": self._output_type.__fields__,
        }
    }
    return spec