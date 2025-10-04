import items.Consumables;
import items.Item;
import items.MedicalSupplies;
import items.Weapons;
import items.characters.Companions;
import items.characters.MainCharacter;
import player.Player;

public class App {
    public static void main(String[] args) throws Exception {
        // Create an Inventory Object
        Inventory inventory = new Inventory();

        // Create Item objects
        Weapons weapon1 = new Weapons("Chinese Sword", 1, 10, "Melee");
        Item item1 = new Item("Bottle Caps", 10000);
        MedicalSupplies medicalSupplies1 = new MedicalSupplies("Stimpack", 100, 75);
        Consumables consumable1 = new Consumables("Nuka Cola", 5, "Drink");

        // store items in the inventory (GENERAL)
        inventory.addItem(medicalSupplies1);
        inventory.addItem(weapon1);
        inventory.addItem(consumable1);
        inventory.addItem(item1 );

        inventory.addItem("Stimpack", 100, 75);
        inventory.addItem("Chinese Sword", 1, 10, "Melee");
        inventory.addItem("Nuka Cola", 5, "Drink");

        // display items in the inventory
        inventory.displayItems();


        // build Player
        MainCharacter player1 = new MainCharacter("Bobby", 100, 1, new Item[]{medicalSupplies1, weapon1, consumable1, item1}) ;

        Companions companion1 = new Companions("Piper", 100, 15, new Item[]{medicalSupplies1, weapon1, consumable1}, true) ;

        Companions companion2 = new Companions("DogMeat", 100, 15, new Item[]{medicalSupplies1, consumable1}, true) ;

        // display player info
        Characters characters = new Characters();
        characters.addCharacter(player1);
        characters.addCharacter(companion1);
        characters.addCharacter(companion2);

        // display players
        characters.displayCharacters();

    }
}
