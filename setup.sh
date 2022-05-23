python3 -m pip install -r requirements.txt
cd duckfetch
sudo cp duckfetch.py /bin/quackfetch
cd ..
sudo alias duckfetch='python3 /bin/quackfetch.py'<
if [ -n "$ZSH_VERSION" ]; then
    echo "zsh detected"
    echo "alias duckfetch='python3 /bin/quackfetch'" >> ~/.zshrc
    source ~/.zshrc
else
    echo "bash detected"
    echo "alias duckfetch='python3 /bin/quackfetch'" >> ~/.bashrc
    source ~/.bashrc
fi
