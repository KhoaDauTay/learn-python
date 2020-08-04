def read(input_file):
    file_name = input_file
    try:
        f = open(file_name,'r')
        read_file = f.read()
        print(read_file)
        f.close()
    except Exception as e:
        print(type(e),e)


def write(input_file):
    file_name = input_file
    try:
        f =open(file_name,'w')
        replace = input("Text Here : ")
        f.write(replace)
    except Exception as e:
        print(type(e),e)

def write_next_text(input_file):
    file_name = input_file
    try:
        f =open(file_name,'a')
        replace = input("Text Here : ")
        f.write(replace)
    except Exception as e:
        print(type(e),e)



write_next_text('..\khoa.txt')
# write('/../khoa.txt')
read('..\khoa.txt')

# read('/../khoa.txt')