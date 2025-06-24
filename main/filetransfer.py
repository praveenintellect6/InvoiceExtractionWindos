import os
import paramiko
def upload_folder(local_dir, remote_dir, hostname, port, username, password):
    transport = paramiko.Transport((hostname, port))
    transport.connect(username=username, password=password)
    sftp = paramiko.SFTPClient.from_transport(transport)

    # Recursive upload
    for root, dirs, files in os.walk(local_dir):
        remote_path = os.path.join(remote_dir, os.path.relpath(root, local_dir)).replace("\\", "/")
        try:
            sftp.mkdir(remote_path)
        except IOError:
            pass  # Folder may already exist

        for file in files:
            local_file = os.path.join(root, file)
            remote_file = os.path.join(remote_path, file).replace("\\", "/")
            sftp.put(local_file, remote_file)
            print(f"Uploaded {local_file} to {remote_file}")

    sftp.close()
    transport.close()


upload_folder(
    local_dir='../media',
    remote_dir = rf"/Desktop",
    hostname='192.168.1.170',
    port=22,
    username='user',
    password='password'
)