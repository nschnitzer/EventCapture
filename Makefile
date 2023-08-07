CC=gcc
CFLAGS=-g

%.o: %.c
	$(CC) -c -o $@ $< $(CFLAGS)


example_progam: example_program.o
	$(CC) -o $@ example_program.o $(CFLAGS)

example_program2: example_program2.o
	$(CC) -o $@ example_program2.o $(CFLAGS)

all:
	make example_program
	make example_program2


clean:
	rm -rf example_program
	rm -rf *.o
