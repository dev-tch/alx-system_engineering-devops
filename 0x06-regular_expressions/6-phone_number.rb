#!/usr/bin/env ruby
# The regular expression must match a 10 digit phone number
pattern=/^\d{10}$/
result_match = ""

if ARGV.length >= 1
  input  = ARGV[0]
  result_match = input.scan(pattern).join
end
puts result_match
