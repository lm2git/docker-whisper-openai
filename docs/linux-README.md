
# Docker Installation Guide on Linux

This guide shows you how to install Docker on a Linux distribution (Ubuntu).

## Steps for installation on Ubuntu (Most common distribution):

1. **Update the system**:
   Open the terminal and run the command to update the system:
   ```bash
   sudo apt-get update
   sudo apt-get upgrade
   ```

2. **Install the necessary dependencies**:
   Install some packages that Docker requires:
   ```bash
   sudo apt-get install apt-transport-https ca-certificates curl software-properties-common
   ```

3. **Add the official Docker repository**:
   Add the official Docker GPG key and the repository:
   ```bash
   curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -
   sudo add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable"
   ```

4. **Install Docker**:
   Now you can install Docker with the following command:
   ```bash
   sudo apt-get update
   sudo apt-get install docker-ce
   ```

5. **Verify the installation**:
   Verify that Docker has been installed correctly by running:
   ```bash
   sudo docker --version
   ```

6. **Start Docker and enable automatic startup**:
   Start the Docker service and enable it to start automatically on system boot:
   ```bash
   sudo systemctl start docker
   sudo systemctl enable docker
   ```

7. **Run Docker without `sudo` (optional)**:
   To run Docker commands without using `sudo`, add your user to the Docker group:
   ```bash
   sudo usermod -aG docker $USER
   ```
   After running this command, you must log out and log back in to apply the changes.

8. **Test the installation**:
   You can test Docker by running the command:
   ```bash
   docker run hello-world
   ```

