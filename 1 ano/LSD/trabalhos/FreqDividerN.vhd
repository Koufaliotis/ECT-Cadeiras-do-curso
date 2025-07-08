library IEEE;
use IEEE.STD_LOGIC_1164.all;
use IEEE.NUMERIC_STD.all;

entity FreqDividerN is
    generic(n     : natural := 8); --clock frequency set
    port(clkIn    : in  std_logic;--eletrical adapter 50Mz
          clkOut    : out std_logic); --output

end FreqDividerN;

architecture Behavioral of FreqDividerN is

    signal aux_divCounter : natural;

begin
    assert(N >= 2);

    process(clkIn)
    begin
        if (rising_edge(clkIn)) then
            if (aux_divCounter = n - 1) then
                clkOut         <= '0';
                aux_divCounter <= 0;
            else
                if (aux_divCounter = (n / 2 - 1)) then
                    clkOut     <= '1';
                end if;
                aux_divCounter <= aux_divCounter + 1;
            end if;
        end if;
    end process;
end Behavioral;