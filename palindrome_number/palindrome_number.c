bool isPalindrome(int x) {
    if (x == 0){
        return true;
    }
    
    if (x<0 || x%10 == 0){
        return false;
    }
    
    int reversed_number = 0;
    while (x>reversed_number){
        reversed_number = reversed_number * 10 + x%10;
        x = floor(x/10);
    }
    if ( x == reversed_number || floor(reversed_number/10)==x){
        return true;
    }
    else{
        return false;
    }
}
