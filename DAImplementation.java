import java.util.HashMap;
import java.util.ArrayList;
import java.io.*;
import java.util.*;
import java.util.Collections;

public class DAImplementation {
    // 1. hashmap 
    HashMap <String, Integer> hashmap = new HashMap<>();
    this.hashmap.put("hi", 1);

    // 2. arraylist
    ArrayList<Integer> lst = new ArrayList<>();
    int maximum = Collections.max(lst);
    // rhs cannot be interface

    // 3. stack
    Stack<Integer> stack = new Stack<>();
    stack.push(1);
    stack.pop();
    stack.contains(1);
    stack.elementAt(2);
    stack.lastElement();

    // 4. trie 
    Trie trie = new Trie();
    trie.put("a");
    trie.put("Hello");
    trie.getRoot();
    trie.getChildren();
    
    // java doesnt have library for trie
    public class Trie {
        static final int ALPHABET_SIZE = 26;
        
        class TrieNode
        {
            TrieNode[] children = new TrieNode[ALPHABET_SIZE];
            boolean isEndOfWord;
            TrieNode(){
                isEndOfWord = false;
                for (int i = 0; i < ALPHABET_SIZE; i++)
                    children[i] = null;
            }
        };
	
	static TrieNode root;

        void insert(String key) {
            int level;
            int length = key.length();
            int index;
        
            TrieNode pCrawl = root;
        
            for (level = 0; level < length; level++) {
                index = key.charAt(level) - 'a';
                if (pCrawl.children[index] == null)
                    pCrawl.children[index] = new TrieNode();
        
                pCrawl = pCrawl.children[index];
            }
                pCrawl.isEndOfWord = true;
        }
        
        boolean search(String key) {
            int level;
            int length = key.length();
            int index;
            TrieNode pCrawl = root;
            for (level = 0; level < length; level++)
            {
                index = key.charAt(level) - 'a';
        
                if (pCrawl.children[index] == null)
                    return false;
        
                pCrawl = pCrawl.children[index];
            }
            return (pCrawl.isEndOfWord);
        }	
    }

    // 5. queue
    List<Integer> queue = new ArrayList<Integer>();
    queue.remove(0);

    // 6. tree
    class Tree {
        class TreeNode {
            int key;
            public TreeNode left = null;
            public TreeNode right = null;
            int weight = 1;
            // contstructor
            TreeNode(int k) {
                key = k;
            }
        }
    }

} 

