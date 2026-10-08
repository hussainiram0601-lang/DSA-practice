import pandas as pd

def last_passenger(queue: pd.DataFrame) -> pd.DataFrame:
    queue = queue.sort_values(by='turn', ascending = True)
    queue['total'] = queue['weight'].cumsum()
    val_person = queue[queue['total']<=1000]
    last_person = val_person.tail(1)[['person_name']]
    return last_person

    
    
        
    