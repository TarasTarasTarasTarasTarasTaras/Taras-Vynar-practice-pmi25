from Observer import Observer

class Event:
    @staticmethod
    def update(key, old_list, list_of_values, pos_or_range, new_list):
        for listener in Observer.listeners:
            if key == listener:
                Observer.listeners[listener](old_list, list_of_values, pos_or_range, new_list)
                return
