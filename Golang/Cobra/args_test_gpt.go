package cobra_test

import (
	"fmt"
	"testing"

	"github.com/spf13/cobra"
)

func TestLegacyArgs(t *testing.T) {
	cmd := &cobra.Command{}
	cmd.AddCommand(&cobra.Command{Use: "child"})

	tests := []struct {
		name    string
		args    []string
		wantErr bool
	}{
		{"No subcommand, no args", []string{}, false},
		{"No subcommand, with args", []string{"arg1"}, false},
		{"With subcommand, invalid arg", []string{"invalid"}, true},
		{"With subcommand, valid arg", []string{"child"}, false},
	}

	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			err := legacyArgs(cmd, tt.args)
			if (err != nil) != tt.wantErr {
				t.Errorf("legacyArgs() error = %v, wantErr %v", err, tt.wantErr)
			}
		})
	}
}

func TestNoArgs(t *testing.T) {
	cmd := &cobra.Command{}

	tests := []struct {
		name    string
		args    []string
		wantErr bool
	}{
		{"No args", []string{}, false},
		{"With args", []string{"arg1"}, true},
	}

	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			err := NoArgs(cmd, tt.args)
			if (err != nil) != tt.wantErr {
				t.Errorf("NoArgs() error = %v, wantErr %v", err, tt.wantErr)
			}
		})
	}
}

func TestOnlyValidArgs(t *testing.T) {
	cmd := &cobra.Command{
		ValidArgs: []string{"valid1", "valid2"},
	}

	tests := []struct {
		name    string
		args    []string
		wantErr bool
	}{
		{"Valid args", []string{"valid1"}, false},
		{"Invalid args", []string{"invalid"}, true},
	}

	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			err := OnlyValidArgs(cmd, tt.args)
			if (err != nil) != tt.wantErr {
				t.Errorf("OnlyValidArgs() error = %v, wantErr %v", err, tt.wantErr)
			}
		})
	}
}

func TestArbitraryArgs(t *testing.T) {
	cmd := &cobra.Command{}

	tests := []struct {
		name    string
		args    []string
		wantErr bool
	}{
		{"No args", []string{}, false},
		{"With args", []string{"arg1"}, false},
	}

	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			err := ArbitraryArgs(cmd, tt.args)
			if (err != nil) != tt.wantErr {
				t.Errorf("ArbitraryArgs() error = %v, wantErr %v", err, tt.wantErr)
			}
		})
	}
}

func TestMinimumNArgs(t *testing.T) {
	cmd := &cobra.Command{}

	tests := []struct {
		name    string
		n       int
		args    []string
		wantErr bool
	}{
		{"Minimum 1 arg, no args", 1, []string{}, true},
		{"Minimum 1 arg, 1 arg", 1, []string{"arg1"}, false},
		{"Minimum 2 args, 1 arg", 2, []string{"arg1"}, true},
	}

	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			err := MinimumNArgs(tt.n)(cmd, tt.args)
			if (err != nil) != tt.wantErr {
				t.Errorf("MinimumNArgs() error = %v, wantErr %v", err, tt.wantErr)
			}
		})
	}
}

func TestMaximumNArgs(t *testing.T) {
	cmd := &cobra.Command{}

	tests := []struct {
		name    string
		n       int
		args    []string
		wantErr bool
	}{
		{"Maximum 1 arg, no args", 1, []string{}, false},
		{"Maximum 1 arg, 2 args", 1, []string{"arg1", "arg2"}, true},
		{"Maximum 2 args, 2 args", 2, []string{"arg1", "arg2"}, false},
	}

	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			err := MaximumNArgs(tt.n)(cmd, tt.args)
			if (err != nil) != tt.wantErr {
				t.Errorf("MaximumNArgs() error = %v, wantErr %v", err, tt.wantErr)
			}
		})
	}
}

func TestExactArgs(t *testing.T) {
	cmd := &cobra.Command{}

	tests := []struct {
		name    string
		n       int
		args    []string
		wantErr bool
	}{
		{"Exact 1 arg, no args", 1, []string{}, true},
		{"Exact 1 arg, 1 arg", 1, []string{"arg1"}, false},
		{"Exact 1 arg, 2 args", 1, []string{"arg1", "arg2"}, true},
		{"Exact 2 args, 2 args", 2, []string{"arg1", "arg2"}, false},
		{"Exact 2 args, 1 arg", 2, []string{"arg1"}, true},
	}

	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			err := ExactArgs(tt.n)(cmd, tt.args)
			if (err != nil) != tt.wantErr {
				t.Errorf("ExactArgs() error = %v, wantErr %v", err, tt.wantErr)
			}
		})
	}
}

func TestRangeArgs(t *testing.T) {
	cmd := &cobra.Command{}

	tests := []struct {
		name    string
		min     int
		max     int
		args    []string
		wantErr bool
	}{
		{"Range 1-2 args, no args", 1, 2, []string{}, true},
		{"Range 1-2 args, 1 arg", 1, 2, []string{"arg1"}, false},
		{"Range 1-2 args, 2 args", 1, 2, []string{"arg1", "arg2"}, false},
		{"Range 1-2 args, 3 args", 1, 2, []string{"arg1", "arg2", "arg3"}, true},
		{"Range 2-3 args, 2 args", 2, 3, []string{"arg1", "arg2"}, false},
		{"Range 2-3 args, 1 arg", 2, 3, []string{"arg1"}, true},
	}

	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			err := RangeArgs(tt.min, tt.max)(cmd, tt.args)
			if (err != nil) != tt.wantErr {
				t.Errorf("RangeArgs() error = %v, wantErr %v", err, tt.wantErr)
			}
		})
	}
}

func TestMatchAll(t *testing.T) {
	cmd := &cobra.Command{}
	cmd.ValidArgs = []string{"valid"}

	tests := []struct {
		name    string
		args    []string
		wantErr bool
	}{
		{"MatchAll valid args", []string{"valid"}, false},
		{"MatchAll invalid args", []string{"invalid"}, true},
		{"MatchAll no args", []string{}, true},
	}

	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			err := MatchAll(ExactArgs(1), OnlyValidArgs)(cmd, tt.args)
			if (err != nil) != tt.wantErr {
				t.Errorf("MatchAll() error = %v, wantErr %v", err, tt.wantErr)
			}
		})
	}
}
