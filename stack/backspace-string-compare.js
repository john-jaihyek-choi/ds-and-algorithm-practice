var backspaceCompare = function (s, t) {
  /*
    Note:
        - # is a backspace character
        - Return
            - True if s == t after backspace removal
            - False if s != t after backspace removal
    Intuition:
        - Stacks for s and t characters:
            - iterate s
                - if character is not #:
                    - push to the stack
                - if character is #:
                    - remove the top of the stack
                    - continue to next iteration
            - repeat for t
            - TC: O(n + m) / SC: O(n + m)
    */

  const stackS = applyBackspaces(s);
  const stackT = applyBackspaces(t);

  return stackS.join() == stackT.join();
};

const applyBackspaces = (string) => {
  const stack = [];

  for (let char of string) {
    if (char === "#") stack.pop();
    else stack.push(char);
  }

  return stack;
};
