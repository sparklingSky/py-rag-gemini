from _0_init_config import config_settings


class APIKey:
    def __init__(self, api_keys_dict):
        self.api_keys = [v["api_key"] for k, v in api_keys_dict.items()]
        self.current_key_index = 0

    def get_current_key(self):
        return self.api_keys[self.current_key_index]

    def rotate_key(self):
        if self.current_key_index < len(self.api_keys) - 1:
            self.current_key_index += 1
            print(
                f"\nThe quota has been exhausted. Switching to API Key #{self.current_key_index + 1} "
                f"out of {len(self.api_keys)}"
            )
            return True
        return False


if __name__ == "__main__":
    key = APIKey(config_settings["api_keys"])
    key.rotate_key()
