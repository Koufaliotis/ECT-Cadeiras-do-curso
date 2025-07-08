--register
LIBRARY IEEE;
USE IEEE.STD_LOGIC_1164.ALL;
use IEEE.NUMERIC_STD.ALL;

entity RegN is
generic (N : integer := 4);
	port(dataIn : in std_logic_vector(N-1 downto 0);
		  dataOut : out std_logic_vector(N-1 downto 0);
		  enable : in std_logic;
		  clock : in std_logic;
		  reset : in std_logic);
end RegN;


architecture Behavioral of RegN is
signal s_dataIn, s_dataOut : unsigned(N-1 downto 0);
begin

	process(clock)
	begin
		if (rising_edge(clock)) then

			if(reset = '1') then
				s_dataOut <= (others => '0');
			else
				if (enable = '1') then
					s_datain <=unsigned(dataIn);
					s_dataOut <= s_dataIn; 

				end if;	
			end if;
		end if;
	
	end process;
	
	dataOut <= std_logic_vector(s_dataOut(N - 1 downto 0));

end Behavioral;