#!/bin/bash

#!/bin/bash

currentdate=$(date +%Y-%m-%d_%H-%M-%S)

rsync_opt="-avb --backup-dir=$currentdate --delete"

$(which rsync) $rsync_opt $1/ $2/current >> back.log
echo "Changing time is $currentdate" >> back.log
