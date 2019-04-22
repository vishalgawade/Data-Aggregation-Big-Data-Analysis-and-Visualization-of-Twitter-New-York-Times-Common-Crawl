
#!/bin/bash -xe
sudo pip-3.6 install nltk pandas numpy textcleaner
sudo python3.6 -m nltk.downloader -d /usr/share/nltk_data all
# sudo easy_install-3.4 pip
# sudo /usr/local/bin/pip3 install paramiko nltk scipy scikit-learn pandas numpy