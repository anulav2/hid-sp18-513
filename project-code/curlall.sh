curl -H "Content-Type: application/json" -X POST -d '{"src_host":"gani-VirtualBox", "src_user":"gani"}' http://localhost:5001/create_ssh_key

curl -H "Content-Type: application/json" -X POST -d '' http://localhost:5002/getstatus/INITIAL_REQUEST

curl -H "Content-Type: application/json" -X POST -d '{"src_host":"gani-VirtualBox", "src_user":"gani", "src_key":"/home/gani/.ssh/id_rsa.pub", "tgt_host":"gani-VirtualBox", "tgt_user":"nemo","req_by":"Uma"}' http://localhost:5003/request_access

curl -H "Content-Type: application/json" -X POST -d '' http://localhost:5004/validate_and_action

curl -H "Content-Type: application/json" -X POST -d '{"src_host":"gani-VirtualBox", "src_user":"gani", "src_pub_key":"/home/gani/.ssh/id_rsa.pub", "tgt_host":"gani-VirtualBox", "tgt_user":"nemo","req_processed_by":"gani"}' http://localhost:5005/copy_ssh_key
