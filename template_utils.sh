#!/bin/bash
echo "==================="
echo "This is the template utils select a option to continue"
echo "1) Replace all template names"
echo "2) Replace file name"
echo "3) Exit"
echo "==================="

# shellcheck disable=SC2162
read option_input
current_dir=${PWD##*/}

function replace_file_name() {
  file_path="${1}"
  name_to_replace="${2}"
  replaced_name="${3}"
  eval "sed -i '' -e 's/${name_to_replace}/${replaced_name}/g' ${file_path}"
}

function replace_folders_name {
  echo "=> Write the name of your project"
  # shellcheck disable=SC2162
  read new_project_name
  eval "mv ${current_dir} ${new_project_name} && cd .. && mv ${current_dir} ${new_project_name} && cd ${new_project_name}"

  for folder_name in "manage.py" "${new_project_name}/asgi.py" "${new_project_name}/settings.py" "${new_project_name}/wsgi.py" "${new_project_name}/urls.py"
  do
   replace_file_name "${folder_name}" "${current_dir}" "${new_project_name}"
  done
}

if [[ $option_input == 1 ]]
then
    replace_folders_name
elif [[ $option_input == 2 ]]
then
  echo "-> Enter the file path that will be replaced"
  # shellcheck disable=SC2162
  read file_path
  echo "-> Enter the word that will be replaced"
  # shellcheck disable=SC2162
  read name_to_replace
  echo "-> Enter the new word to put in the file"
  # shellcheck disable=SC2162
  read replaced_name
  replace_file_name "${file_path}" "${name_to_replace}" "${replaced_name}"
else
    echo "==> Good bye"
fi

