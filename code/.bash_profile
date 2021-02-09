export CLICOLOR=1
export PATH=/usr/local/bin:$PATH
alias typora="open -a typora"
alias nav='. ~/bash/nav.sh'
alias mysql=/usr/local/mysql/bin/mysql
alias mysqladmin=/usr/local/mysql/bin/mysqladmin

# >>> conda initialize >>>
# !! Contents within this block are managed by 'conda init' !!
__conda_setup="$('/Users/zhouxu/miniconda3/bin/conda' 'shell.bash' 'hook' 2> /dev/null)"
if [ $? -eq 0 ]; then
    eval "$__conda_setup"
else
    if [ -f "/Users/zhouxu/miniconda3/etc/profile.d/conda.sh" ]; then
        . "/Users/zhouxu/miniconda3/etc/profile.d/conda.sh"
    else
        export PATH="/Users/zhouxu/miniconda3/bin:$PATH"
    fi
fi
unset __conda_setup
# <<< conda initialize <<<

