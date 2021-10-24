class Observer:
    listeners = dict()
    
    @staticmethod
    def attach(key, function):
        Observer.listeners[key] = function

    @staticmethod
    def detach(key):
        Observer.listeners.pop(key)
