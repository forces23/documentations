package items.characters;

import items.Item;
import player.Player;

public class Companions extends Player {
    private boolean recruited;

    public Companions(String name, int healthPoints, int level, Item[] inventory, boolean recruited) {
        super(name, healthPoints, level, inventory);
        this.recruited = recruited;
    }

    public boolean setRecruited() {
        return recruited;
    }

    public void getRecruited(boolean recruited) {
        this.recruited = recruited;
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
        System.out.println("Companion Name: " + getName() + " || Health Points: " + getHealthPoints() + " || Level: "
                + getLevel() + " || Inventory: {" + displayItems() + "} || Recruited: " + recruited);

    }
}
