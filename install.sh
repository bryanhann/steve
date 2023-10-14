[ ! $0 == ./install.sh ] && echo try ./install.sh && exit
dt=$(date '+%Y%m%dT%H%M%S')

for d in profile bashrc; do
    echo $d
    s=${PWD}/dots/$d
    t=${HOME}/.$d
    [ -f $t ] && [ ! -h $t ] && cp $t ${t}.backup.${dt}
    [ -f $t ] && rm $t
    ln -s $s $t
done
exit
ln -s ${PWD}/dots/bashrc ~/.profile
rm ~/.bashrc
ln -s ${PWD}/dots/bashrc ~/.bashrc
