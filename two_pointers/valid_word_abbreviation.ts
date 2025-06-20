function validWordAbbreviation(word: string, abbr: string): boolean {
  /*
    Intuition:
        - keep track of i index while iterating
    */
  if (
    word.length === abbr.length &&
    word !== abbr &&
    Number(abbr) !== word.length
  ) {
    return false;
  }

  let p = 1;
  let temp = 0;
  for (let i = 1; i < abbr.length; i++) {
    if (Number(abbr[i])) {
      temp = temp * 10 + Number(abbr[i]);
    } else {
      p += temp;
      console.log(
        `p: ${p} vs i: ${i} / ${abbr[i]} vs ${word[p]} / temp: ${temp}`
      );
      if (abbr[i] !== word[p]) {
        return false;
      }
      temp = 0;
      p++;
    }
  }

  return true;
}
