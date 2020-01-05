#!bin/bash

if [ $# -eq 0 ]; then
    cat << EOF 
usage: track start <label>
        track stop
        track status
EOF
    exit
fi

command="$1"
label="$2"

case "$command" in
    "start")
        if [[ $(tail "$LOGFILE" -n 1) == LABEL* ]]; then
            echo "A timer is already running"
            exit
        else
            echo "Timer starting"
            # printf "START $(date +"%F %T")\nLABEL $label\n" >> "$LOGFILE"
            printf "START $(date)\nLABEL $label\n" >> "$LOGFILE"
        fi
        ;;
    "stop")
        if [[ $(tail "$LOGFILE" -n 1) == LABEL* ]]; then
            echo "Timer stopping"
            printf "END $(date)\n\n" >> "$LOGFILE"
        else
            echo "No timer is currently running"
            exit
        fi
        ;;
    "status")
        lastline=$(tail "$LOGFILE" -n 1)
        if [[ "$lastline" == LABEL* ]]; then
            echo "Timer running:"
            echo "$lastline" | cut -d' ' -f2-
	      else
	          echo "No timer running"
	      fi
	      ;;
    "log")
        cat "$LOGFILE" | while read p; do
            prefix=$(echo "$p" | cut -d' ' -f1)
            case "$prefix" in
                "START")
                    start=$(echo "$p" | cut -d' ' -f2-)
                    start=$(date --date="$start" +"%s")
                    ;;
                "LABEL")
                    label=$(echo "$p" | cut -d' ' -f2-)
                    ;;
                "END")
                    stop=$(echo "$p" | cut -d' ' -f2-)
                    stop=$(date --date="$stop" +"%s")
                    diff=$(echo "$stop - $start" | bc)
                    diff=$(date --date=@"$diff" -u +"%H:%M:%S")
                    echo "$label: $diff"
                    ;;
            esac
        done 
        ;;
    *)
	      echo "$command: Not a valid command"
	      ;;
esac
