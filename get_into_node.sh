#!/usr/bin/env bash

function master {
  echo "Getting into master..."
  docker exec -it master bash
}

function worker1 {
  echo "Getting into worker 1..."
  docker exec -it worker1 bash
}

function worker2 {
  echo "Getting into worker 2..."
  docker exec -it worker2 bash
}

case $1 in
  master )
  master
    ;;

  worker1 )
  worker1
    ;;

  worker2 )
  worker2
    ;;

  * )
  printf "ERROR: Missing command\n  Usage: `basename $0` (master|worker1|worker2)\n"
  exit 1
    ;;
esac