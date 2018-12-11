def main(args)
  if name = args["name"]?
    return {"greeting" => "Hello #{name}!"}
  else
    return {"greeting" => "Hello swif4!"}
  end
end

# puts main({} of String => String)
# puts main({"name": "justin"})
