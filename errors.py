from functools import wraps

def input_error(func):
    @wraps(func)
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError as e:
            msg = str(e).strip()
            if not msg or msg == "ValueError":
                name = func.__name__
                if name == "handle_add":
                    return "Give me name and phone please."
                if name == "handle_change":
                    return "Give me name and new phone please (or name old_phone new_phone)."
                if name == "handle_phone":
                    return "Enter user name."
                if name == "handle_addphone":
                    return "Give me name and phone please."
                if name == "handle_removephone":
                    return "Give me name and phone to remove."
                if name == "handle_delete":
                    return "Enter user name to delete."
                if name == "handle_find":
                    return "Enter user name to find."
                return "Enter the argument for the command"
            return msg
        except KeyError:
            return "Contact not found."
        except IndexError:
            return "Enter the argument for the command"
    return inner
