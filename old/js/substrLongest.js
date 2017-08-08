/*
Given a string, find the length of the longest substring without repeating characters.

Examples:

Given "abcabcbb", the answer is "abc", which the length is 3.

Given "bbbbb", the answer is "b", with the length of 1.

Given "pwwkew", the answer is "wke", with the length of 3. Note that the answer must be a substring, "pwke" is a subsequence and not a substring.
 */


/**
 * @param {string} s
 * @return {number}
 */

var debug=1;
var lengthOfLongestSubstring = function(s) {
  if(s.length<2) return s.length;
  var o={};
  o[s[0]]=1;
  o.start=0;

  for(var i=1, j=2; j<=s.length+1; j++){
    if(j==s.length+1){
      var len=j-i;

      if(!o.len || len> o.len){
        o.len=len;
        o.start=i-1;
      }
      continue;
    }
    if(j<=i) continue;
    if(o[s[j-1]] && o[s[j-1]]>= i){

      if(debug)console.info('got: '+s[i-1]+(i-1)+'-'+s[j-1]+(j-1));
      var len=j-i;

      if(!o.len || len> o.len){
        o.len=len;
        o.start=i-1;
      }
      i=o[s[j-1]]+1;
    }
    if (debug)console.info(s[i-1]+(i-1)+'-'+s[j-1]+(j-1));
    o[s[j-1]]=j;

  }
  if(!o.len ) o.len=s.length;
  if(debug)console.info('longest: '+o.len+', v: '+s.substr(o.start, o.len));
  return o.len;

};


lengthOfLongestSubstring("abcabcbb");
lengthOfLongestSubstring("aa");
lengthOfLongestSubstring("");
lengthOfLongestSubstring("pwwkew");
lengthOfLongestSubstring("au");
lengthOfLongestSubstring("aab");
