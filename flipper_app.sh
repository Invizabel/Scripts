clear

rm -rf ~/Downloads/flipper-application-catalog
rm -rf ~/Downloads/qApps/

mkdir ~/Downloads/qApps/

touch ~/Downloads/qApps/errors.log

cd ~/Downloads
git clone https://github.com/flipperdevices/flipper-application-catalog
cd ~/Downloads/flipper-application-catalog/applications

let "count=0"
find -follow | grep .yml | while IFS= read -r line; do
    cd ~/Downloads/flipper-application-catalog/applications
    rm -rf temp
    mkdir temp
    echo $line
    ((count++))
    if python3 -u ~/Downloads/flipper-application-catalog/tools/bundle.py --nolint $line "bundle_$count.zip" 2>&1 | grep -qi 'error'; then echo $line >> ~/Downloads/qApps/errors.log; continue; fi
    cp bundle_$count.zip temp
    cd temp
    unzip ~/Downloads/flipper-application-catalog/applications/temp/bundle_$count.zip
    cd ~/Downloads/flipper-application-catalog/applications/temp/code/
    python3 -m ufbt
    cd ~/Downloads/flipper-application-catalog/temp/applications
    cp ~/Downloads/flipper-application-catalog/applications/temp/code/dist/*.fap ~/Downloads/qApps/
    rm -rf code
done
rm -rf ~/Downloads/flipper-application-catalog
