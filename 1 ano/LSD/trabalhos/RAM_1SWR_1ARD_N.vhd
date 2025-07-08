library IEEE;
use IEEE.STD_LOGIC_1164.all;
use IEEE.NUMERIC_STD.all;

ENTITY RAM_1SWR_1ARD_N IS
	generic(BitsOfAddress  : natural := 4;
			  BitsInDataOfAddress : natural := 8); --clock frequency set
	port(Clk : in std_logic;
		  WriteEnable : in std_logic;
		  WriteAddress : in std_logic_vector(BitsOfAddress -1 downto 0);--write in one adress of 16case
		  WriteData : in std_logic_vector(BitsInDataOfAddress -1 downto 0);--data in 8 bits 
		  readAddress : in std_logic_vector(BitsOfAddress -1 downto 0); --read in address on
		  readData : out std_logic_vector(BitsInDataOfAddress -1 downto 0));
end RAM_1SWR_1ARD_N;

architecture Behavioral of RAM_1SWR_1ARD_N is
		subtype TDataWord is std_logic_vector(BitsInDataOfAddress -1 downto 0);
		type TMemory is array (0 to 2 * BitsOfAddress -1) of TDataWord;
		signal s_memory : TMemory;
		
begin
		process(Clk)
					begin
						if (rising_edge(Clk)) then
							if (writeEnable = '1') then
								s_memory(to_integer(unsigned(writeAddress))) <= writeData;
							end if;
						end if;
					end process;

readData <= s_memory(to_integer(unsigned(readAddress)));
end Behavioral;