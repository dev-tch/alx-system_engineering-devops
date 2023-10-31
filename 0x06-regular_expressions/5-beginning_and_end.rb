#!/usr/bin/env ruby
# The regular expression must be exactly matching a string that starts with h ends with n and can have any single character in between
pattern=/^h.n$/
result_match = ""

if ARGV.length >= 1
  input  = ARGV[0]
  result_match = input.scan(pattern).join
end
puts result_match
