#!/usr/bin/env ruby
#Find the regular expression that will match the above cases
pattern=/hbt+n/
result_match = ""

if ARGV.length >= 1
  input  = ARGV[0]
  result_match = input.scan(pattern).join
end
puts result_match
