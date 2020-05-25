
# Disable onboard audio device (to enable USB device)
echo " - Disabling on-board audio device"
sudo sed -i "s|options snd-usb-audio index=-2|#options snd-usb-audio index=-2|" /lib/modprobe.d/aliases.conf
echo "blacklist snd_bcm2835" | sudo tee -a /etc/modprobe.d/raspi-blacklist.conf

