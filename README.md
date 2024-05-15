1. Run the following command:
    >>> sh install_parser.sh

2. Run the following commands to install and complile apertium dictionay:
    >>>	sudo apt-get update
    >>> sudo apt-get install lttoolbox
    >>> sudo apt-get install apertium
	>>> sh compile_dict.sh

3. Run the following command to install wxconv:
    >>> pip3 install WXC
	>>> pip3 install wxconv

4. Copy wx_utf8, utf8_wx and ir_no@ files to bin folder:
	>>> cd /usr/bin/
	>>> sudo cp ~/concept_index_dependency-generator/wx_utf8 .
	>>> sudo cp ~/concept_index_dependency-generator/utf8_wx .
	>>> sudo cp ~/concept_index_dependency-generator/ir_no@ .


5. Change the permissions of wx_utf8, utf8_wx and ir_no@ files:
	>>> sudo chmod +777 utf8_wx
	>>> sudo chmod +777 wx_utf8 
	>>> sudo chmod +777 ir_no@	


=======================================================================

How to run:

1. Keep the Hindi Sentences with their unique IDs separated with space in 'input_sentences' file.

2. To get the output with Hindi Parser, run the following command:
    >>> python3 run_parser.py
    Output will be stored in the 'HINDI_PARSER_USR' folder.

3. To get the output with Dependency Mapper, run the following command:
    >>> python3 run_mapper.py
    Output will be stored in the 'DEPENDENCY_MAPPER_USR' folder.