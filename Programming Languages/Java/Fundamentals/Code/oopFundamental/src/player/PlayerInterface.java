package player;

import items.Item;

public interface PlayerInterface {
    String getName();
    void setName(String name);
    int getHealthPoints();
    void setHealthPoints(int healthPoints);
    int getLevel();
    void setLevel(int level);
    Item[] getInventory();
    void setInventory(Item[] inventory);
    void displayPlayerInfo();
}
