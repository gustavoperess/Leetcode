#include <sys/socket.h>
#include <string.h>
#include <fcntl.h>
#include <sys/types.h>
#include <unistd.h>
#include <netinet/in.h>
#include <arpa/inet.h>
#include <stdio.h>
#include <stdlib.h>
#include <sys/stat.h>
#include <sys/uio.h>


// a simple server with a get request, with the single goal to learn how server/get requests work.
int main() {
    int s = socket(PF_INET, SOCK_STREAM, 0);
    if (s < 0) {
        perror("socket");
        exit(1);
    }

    struct sockaddr_in addr;
    memset(&addr, 0, sizeof(addr));
    addr.sin_family = AF_INET;
    addr.sin_port = htons(8080); 
    addr.sin_addr.s_addr = INADDR_ANY;

    if (bind(s, (struct sockaddr *)&addr, sizeof(addr)) < 0) {
        perror("bind");
        close(s);
        exit(1);
    }

    if (listen(s, 10) < 0) {
        perror("listen");
        close(s);
        exit(1);
    }

    printf("Server listening on port 8080\n");

    int client_fd = accept(s, NULL, NULL);
    if (client_fd < 0) {
        perror("accept");
        close(s);
        exit(1);
    }

    char buffer[1024] = {0};
    if (recv(client_fd, buffer, sizeof(buffer), 0) < 0) {
        perror("recv");
        close(client_fd);
        close(s);
        exit(1);
    }

    printf("Received request: %s\n", buffer);

    char *f = buffer + 5;
    char *space = strchr(f, ' ');
    if (space) {
        *space = 0;
    } else {
        fprintf(stderr, "Invalid request format\n");
        close(client_fd);
        close(s);
        exit(1);
    }

    int opened_fd = open(f, O_RDONLY);
    if (opened_fd < 0) {
        perror("open");
        close(client_fd);
        close(s);
        exit(1);
    }

    struct stat file_stat;
    if (fstat(opened_fd, &file_stat) < 0) {
        perror("fstat");
        close(opened_fd);
        close(client_fd);
        close(s);
        exit(1);
    }


    char response_header[] =
        "HTTP/1.1 200 OK\r\n"
        "Content-Type: text/html\r\n"
        "Content-Length: %ld\r\n"
        "Connection: close\r\n"
        "\r\n";
    dprintf(client_fd, response_header, file_stat.st_size);


    off_t offset = 0;
    sendfile(opened_fd, client_fd, offset, &file_stat.st_size, NULL, 0);

    close(opened_fd);
    close(client_fd);
    close(s);
    return 0;
}
