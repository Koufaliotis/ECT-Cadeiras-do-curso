--contador
LIBRARY IEEE;
USE IEEE.STD_LOGIC_1164.ALL;
USE IEEE.NUMERIC_STD.ALL;
entity Counter is
	port(
		  enable : in std_logic;
		  reset : in std_logic;
		  clock : in std_logic;
		  operation : in std_logic;
		  dataOut : out std_logic_vector(3 downto 0));
		
	end Counter;
	
architecture Behavioral of Counter is
	signal s_cntValue : unsigned(3 downto 0);
begin
		process(clock)
		begin
			if (reset = '1' or s_cntValue >=12) then
				s_cntValue <= (others => '0');
			elsif (rising_edge(clock)) then
				if (enable = '1') then
					if(operation = '0') then
						s_cntValue <= s_cntValue + 1;
					else
						s_cntValue <= s_cntValue - 1;
					end if;
				
				end if;
			end if;
		end process;

dataOut <= std_logic_vector(s_cntValue);
end Behavioral;