CC=gcc
CFLAGS=-g

%.o: %.c
	$(CC) -c -o $@ $< $(CFLAGS)


example_progam: example_program.o
	$(CC) -o $@ example_program.o


all: example_program


clean:
	rm -rf example_program
	rm -rf *.o
