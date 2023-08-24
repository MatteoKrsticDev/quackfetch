python3 -m pip install -r requirements.txt
cd quackfetch
sudo cp quackfetch.py /bin/quackfetch
cd ..
sudo alias quackfetch='python3 /bin/quackfetch.py'<
if [ -n "$ZSH_VERSION" ]; then
    echo "zsh detected"
    echo "alias quackfetch='python3 /bin/quackfetch'" >> ~/.zshrc
    source ~/.zshrc
else
    echo "bash detected"
    echo "alias quackfetch='python3 /bin/quackfetch'" >> ~/.bashrc
    source ~/.bashrc
fi
