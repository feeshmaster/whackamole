class Config:
    def __init__(self, config=None):
        if config is not None:
            for key, value in config.items():
                setattr(self, key, value)


                #I HATE having to type [""] so i made this