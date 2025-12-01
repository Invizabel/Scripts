rm -rf flipper_venv
python3 -m venv flipper_venv
source flipper_venv/bin/activate

clear

rm -rf ~/Downloads/flipper-application-catalog
rm -rf ~/Downloads/qApps/

mkdir ~/Downloads/qApps
mkdir ~/Downloads/qApps/Bluetooth
mkdir ~/Downloads/qApps/GPIO
mkdir ~/Downloads/qApps/Games
mkdir ~/Downloads/qApps/Infrared
mkdir ~/Downloads/qApps/Media
mkdir ~/Downloads/qApps/NFC
mkdir ~/Downloads/qApps/RFID
mkdir ~/Downloads/qApps/Sub-GHz
mkdir ~/Downloads/qApps/Tools
mkdir ~/Downloads/qApps/USB
mkdir ~/Downloads/qApps/iButton

touch ~/Downloads/qApps/errors.log

cd ~/Downloads
git clone https://github.com/flipperdevices/flipper-application-catalog
pip install -r ~/Downloads/flipper-application-catalog/tools/requirements.txt
cd ~/Downloads/flipper-application-catalog/applications/Bluetooth

let "count=0"
find -follow | grep .yml | while IFS= read -r line; do
    cd ~/Downloads/flipper-application-catalog/applications/Bluetooth
    rm -rf temp
    mkdir temp
    echo $line
    ((count++))
    if python3 -u ~/Downloads/flipper-application-catalog/tools/bundle.py --nolint $line "bundle_$count.zip" 2>&1 | grep -qi 'error'; then echo $line >> ~/Downloads/qApps/errors.log; continue; fi
    cp bundle_$count.zip temp
    cd temp
    unzip ~/Downloads/flipper-application-catalog/applications/Bluetooth/temp/bundle_$count.zip
    cd ~/Downloads/flipper-application-catalog/applications/Bluetooth/temp/code/
    python3 -m ufbt
    cp ~/Downloads/flipper-application-catalog/applications/Bluetooth/temp/code/dist/*.fap ~/Downloads/qApps/Bluetooth
    rm -rf code
done
rm -rf ~/Downloads/flipper-application-catalog
rm -rf flipper_venv
