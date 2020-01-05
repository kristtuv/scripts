#!/bin/bash
lenargs=$#
args=("$@")
function helpmessage {
    echo 'usage: rename filename_form newfilename_form
    example: rename \(*\) blahblah*'
}

function rename {
    echo $args
}
rename
# echo arg
# function rename {
#     if [[ $lenargs -ne 2 ]]; then
#         helpmessage;
#         return;
#     fi

#     for filename in $(ls); do
      
#         # echo$args[0]
#         # echo $2
#     done
# }
# rename
# # function rename {
# # for i in $( command -p ls ); do
# #     # mv $i ${i#INF3331-}
# #     echo "hei" 
# # done
# # }
