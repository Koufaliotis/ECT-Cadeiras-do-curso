LIBRARY IEEE;
USE IEEE.STD_LOGIC_1164.ALL;
USE IEEE.NUMERIC_STD.ALL;

entity ROM_16x8 is
	port(address : in std_logic_vector(3 downto 0 );--the cases in binary
		  dataOut : out std_logic_vector(7 downto 0));--? out of 8 bits

end ROM_16x8;

architecture Behavioral of ROM_16x8 is
	subtype TDataWord is std_logic_vector(7 downto 0); --word size 8 bits
	type ST_ROM is array (0 to 15) of TDataword;
	constant c_memory: ST_ROM := (x"00",
										  x"01",
										  x"02",
										  x"03",
										  x"04",
										  x"05",
										  x"06",
										  x"07",
										  x"08",
										  x"09",
										  x"10",
										  x"11",
										  x"12",
										  x"13",
										  x"14",
										  x"15");
	
	begin
	dataOut <= c_memory(to_integer(unsigned(address)));
end behavioral;