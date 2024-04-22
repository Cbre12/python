class Television:
    MIN_VOLUME = 0
    MAX_VOLUME = 2
    MIN_CHANNEL = 0
    MAX_CHANNEL = 3
    
    def __init__(self):
        """Initialize Television object."""
        self.__muted = False
        self.__volume = Television.MIN_VOLUME
        self.__status = False
        self.__channel = Television.MIN_CHANNEL

    def power(self) -> None:
        """Toggle the power status of the television."""
        if self.__status:
            self.__status = False
            self.__muted = False  # Unmute when powered off
        else:
            self.__status = True

    def mute(self) -> None:
        """Mute or unmute the television."""
        if self.__status:
            if self.__muted:
                self.__muted = False
            else:
                self.__muted = True

    def channel_up(self) -> None:
        """Increase the channel number by 1."""
        if self.__status:
            if self.__channel < Television.MAX_CHANNEL:
                self.__channel += 1
            else:
                self.__channel = Television.MIN_CHANNEL

    def channel_down(self) -> None:
        """Decrease the channel number by 1."""
        if self.__status:
            if self.__channel > Television.MIN_CHANNEL:
                self.__channel -= 1
            else:
                self.__channel = Television.MAX_CHANNEL

    def volume_up(self) -> None:
        """Increase the volume level by 1."""
        if self.__status:
            if self.__volume < Television.MAX_VOLUME:
                self.__volume += 1
                self.__muted = False  # Unmute when volume is adjusted

    def volume_down(self) -> None:
        """Decrease the volume level by 1."""
        if self.__status:
            if self.__volume > Television.MIN_VOLUME:
                self.__volume -= 1
                self.__muted = False  # Unmute when volume is adjusted

    def __str__(self) -> str:
        """Return string representation of the television."""
        if self.__status:
            if self.__muted:
                return f"Power = ON, Channel = {self.__channel}, Volume = Muted"
            else:
                return f"Power = ON, Channel = {self.__channel}, Volume = {self.__volume}"
        else:
            return "Power = False, Channel = 0, Volume: 0"

        
        
