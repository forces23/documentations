package items.characters;

import items.Item;
import player.Player;

public class MainCharacter extends Player {

    public MainCharacter(String name, int healthPoints, int level, Item[] inventory) {
        super(name, healthPoints, level, inventory);
    }

    private String displayItems() {
        String playerItems = "";
        Item[] inventory = getInventory();

        for (int i = 0; i < inventory.length; i++) {
            if (i < inventory.length - 1) {
                playerItems += inventory[i].getName() + ", ";
                continue;
            } else {
                playerItems += inventory[i].getName();
            }

        }

        return playerItems;
    }

    @Override
    public void displayPlayerInfo() {
        System.out.println("Player Name: " + getName() + " || Health Points: " + getHealthPoints() + " || Level: "
                + getLevel() + " || Inventroy: {" + displayItems() + "}");

    }
}
