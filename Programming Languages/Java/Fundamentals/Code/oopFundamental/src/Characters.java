import java.util.ArrayList;
import player.Player;

public class Characters {
    private ArrayList<Player> characters;
    
    public Characters() {
        characters = new ArrayList<>();
    }

    public ArrayList<Player> getCharacters() {
        return characters;
    }

    public void addCharacter(Player character) {
        characters.add(character);
    }

    public void displayCharacters() {
        for(Player character : characters) {
            character.displayPlayerInfo();
        }
    }
}
